# -*- coding: gb2312 -*-
import numpy as np
# ����,�ֶ���,����,ũ����4����������ƻ��,��,�㽶,���Ӻ�â��5��ˮ��,ʹ��numpy��ndarrayʵ�����¹���
# ����һά����ֱ𴢴泬�к�ˮ��������
shop = np.array(['����', '�ֶ���', '����', 'ũ����'])
print('shop:')
print(shop)
print('------------------')
fruit = np.array(['ƻ��', '�㽶', '����','⨺���', 'â��'])
print('fruit:')
print(fruit)
print('------------------')
# ����һ��4*4�Ķ�ά����,�ֱ𴢴�۸�,���м۸���4-10Ԫ֮��
price = np.random.uniform(4, 10, size=(4, 5))
print('price:')
print(price)
print('------------------')
# ѡ����󷢵�ƻ�����������㽶,�����۸�����һԪ
##��ѡ����󷢵�ƻ��,�����1
# var1 = price[shop == '����'][:, fruit == 'ƻ��'] + 1
# var2 = price[shop == '����'][:, fruit == '�㽶'] + 1
# var1 = var1[0][0]
# var2 = var2[0][0]

print('ѡ��:')
print(price[(shop == '����') | (shop == '����'), (fruit == 'ƻ��') | (fruit == '�㽶')])

price[np.where(shop == '����')[0][0]][np.where(fruit == 'ƻ��')[0][0]] += 1
price[np.where(shop == '����')[0][0]][np.where(fruit == '�㽶')[0][0]] += 1
# np.where���ص���һ��Ԫ��(array([?], dtype=int64),) ������shop��fruit����һά��,��ֻ��һ��Ԫ��
# ��np.where()[0]ȡ���õ�����һ���б�,�б�����һ��Ԫ����Ѱ�ҵ�Ԫ���ڶ�Ӧarray�е�λ��
# np.where()[0][0]�ǽ��б��еĵ�һ��Ԫ��ȡ��,Ҳ�����������±�
print('-----------new price------------')
print(price)
print('---------------')
# ũ���̵�ˮ�������,�����е�ˮ���۸����2Ԫ
# price[np.where(shop == 'ũ����')[0][0]] -= 2
price[shop == 'ũ����', :] -= 2
print('-----------new price------------')
print(price)
print('---------------')
# ͳ��4������ƻ����â�������۾���
means = price[:, (fruit == 'ƻ��') | (fruit == 'â��')].mean(axis=0)
##��ѡ��ȫ��������  �ո�:�ո� ������ʾ,���пո����ʡ�����оͱ����: �������
print('ƽ��������:')
print('ƻ��'+str(means[0]))
print('â��'+str(means[1]))
# �ҳ����Ӽ۸����ĳ�������
name = shop[price[:, (fruit == '����')].argmax()]
print(name)
